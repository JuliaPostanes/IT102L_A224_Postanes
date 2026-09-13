import streamlit as st

import postanes_bank_auth
import postanes_bank_storage
import postanes_bank_transactions
import postanes_bank_analysis
import postanes_bank_utils
import pandas as pd
import matplotlib.pyplot as plt


# LAYOUT THINGY
def inject_custom_css():
    st.markdown("""
    <style>
    /* Buttons */
    .stButton>button {
        border-radius: 12px;
        font-weight: 1250;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 900;
        color: #2c2c2c;
    }

    /* Sidebar text */
    .css-1d391kg, .css-1v3fvcr {
        font-weight: 700;
    }

    /* Metrics */
    .stMetric {
        border: 2px solid #6c63ff;
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 10px;
    }
    .stMetric label {
        font-weight: 800;
    }

    /* Sidebar box */
    .css-1d391kg {
        border: 2px solid #999;
        border-radius: 8px;
        padding: 6px;
    }

    /* Section headers with background */
    h2 {
        background-color: #f0f0f0;
        padding: 6px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Postanes Bank",
    page_icon="🏦",
    layout="centered"
)


# ==========================================
#   LE TRANSACTION HELPER
# ==========================================
# Shared by the Deposit and Withdraw menu
# items below, which repeated the same validate, applying it,
# saving it, recording it and show-result the sequence twice.

def handle_transaction(
    account,
    transaction_type,
    amount
):

    if not postanes_bank_utils.is_valid_amount(
        amount
    ):

        st.error(
            f"Invalid {transaction_type.lower()} amount."
        )

        return

    if transaction_type == "Withdraw":

        if amount > account.check_balance():

            st.error(
                "Insufficient balance."
            )

            return

        success = account.withdraw(
            amount
        )

        fail_message = (
            "Withdrawal exceeds the "
            "allowed limit for this account."
        )

    else:

        success = account.deposit(
            amount
        )

        fail_message = "Deposit failed."

    if not success:

        # An example of this is if a StudentAccount rejecting a
        # withdrawal above its limit even
        # though the balance covers it.
        st.error(fail_message)

        return

    postanes_bank_storage.update_account(
        account
    )

    postanes_bank_transactions.record_transaction(
        account,
        transaction_type,
        amount
    )

    st.success(
        f"{transaction_type} successful."
    )

    st.metric(
        "New Balance",
        postanes_bank_utils
        .format_currency(
            account.check_balance()
        )
    )


# ==========================================
# BANKING PAGES
# ==========================================
# Each of these used to be an "elif menu == ..."
# branch. They're plain functions now so they
# can be registered with st.navigation() below,
# which gives a real nav widget (with reliable
# active-page highlighting) instead of a radio
# list styled to look like one.

def dashboard_page():

    account = st.session_state.account

    st.header(
        f"Welcome, {account.account_name}"
    )

    st.subheader(
        "Account Overview"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Balance",
        postanes_bank_utils
        .format_currency(
            account.check_balance()
        )
    )

    col2.metric(
        "Account Type",
        account.get_account_type()
    )

    col3.metric(
        "Account Number",
        account.account_number
    )

    st.divider()

    st.info(
        "Select a banking service from "
        "the menu on the left."
    )


def deposit_page():

    account = st.session_state.account

    st.header(
        "Deposit Money"
    )

    st.write(
        f"Current Balance: "
        f"**{postanes_bank_utils.format_currency(account.check_balance())}**"
    )

    amount = st.number_input(
        "Deposit Amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button(
        "Confirm Deposit",
        type="primary",
        icon="💰",
        use_container_width=True
    ):

        handle_transaction(
            account,
            "Deposit",
            amount
        )

# GOALS PAGE (NEW THING)

def goals_page():
    account = st.session_state.account
    st.header("Savings Goals")

    # SAVED SESSIONS
    if "savings_target" not in st.session_state:
        st.session_state.savings_target = 0.0
    if "savings_deadline" not in st.session_state:
        st.session_state.savings_deadline = None

    
    target = st.number_input(
        "Set Savings Target",
        min_value=0.0,
        step=100.0,
        format="%.2f",
        value=st.session_state.savings_target,
        key="savings_target"
    )

    deadline = st.date_input(
        "Target Date",
        value=st.session_state.savings_deadline,
        key="savings_deadline"
    )

    current_balance = account.check_balance()

    if target > 0:
        progress = min(current_balance / target, 1.0)
        st.progress(progress)
        st.write(f"Progress: {progress*100:.1f}%")

        # METRICS
        st.metric("Current Balance", postanes_bank_utils.format_currency(current_balance))
        st.metric("Target Amount", postanes_bank_utils.format_currency(target))
        if deadline:
            st.metric("Deadline", deadline.strftime("%B %d, %Y"))


def withdraw_page():

    account = st.session_state.account

    st.header(
        "Withdraw Money"
    )

    st.write(
        f"Available Balance: "
        f"**{postanes_bank_utils.format_currency(account.check_balance())}**"
    )

    amount = st.number_input(
        "Withdrawal Amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button(
        "Confirm Withdrawal",
        type="primary",
        icon="💸",
        use_container_width=True
    ):

        handle_transaction(
            account,
            "Withdraw",
            amount
        )


def history_page():

    account = st.session_state.account

    st.header(
        "Transaction History"
    )

    transactions = (
        postanes_bank_transactions
        .get_transactions()
    )

    # Shows only the transactions
    # belonging to the logged-in user.

    transactions = [
        transaction
        for transaction in transactions
        if transaction.get(
            "account_number"
        ) == account.account_number
    ]

    if transactions:

        display_data = []

        for transaction in transactions:

            display_data.append({

                "Timestamp":
                    transaction.get(
                        "timestamp",
                        "N/A"
                    ),

                "Transaction":
                    transaction.get(
                        "transaction",
                        "N/A"
                    ),

                "Amount":
                    postanes_bank_utils
                    .format_currency(
                        transaction.get(
                            "amount",
                            0
                        )
                    ),

                "Balance After":
                    postanes_bank_utils
                    .format_currency(
                        transaction.get(
                            "balance_after",
                            0
                        )
                    )
            })

        st.dataframe(
            display_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No transaction history available."
        )

def analysis_page():

    account = st.session_state.account

    st.header(
        "Transaction Analysis"
    )

    result = (
        postanes_bank_analysis
        .analyze_transactions(
            account.account_number
        )
    )

    # ==================================
    # ANALYSIS 1
    # TRANSACTION SUMMARY
    # ==================================

    st.subheader(
        "1. Transaction Summary"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        result[
            "total_transactions"
        ]
    )

    col2.metric(
        "Deposits",
        result[
            "deposits"
        ]
    )

    col3.metric(
        "Withdrawals",
        result[
            "withdrawals"
        ]
    )

    st.divider()

    # ==================================
    # ANALYSIS 2
    # MONEY FLOW
    # ==================================

    st.subheader(
        "2. Money Flow Analysis"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Deposited",
        postanes_bank_utils
        .format_currency(
            result[
                "total_deposited"
            ]
        )
    )

    col2.metric(
        "Total Withdrawn",
        postanes_bank_utils
        .format_currency(
            result[
                "total_withdrawn"
            ]
        )
    )

    col3.metric(
        "Net Cash Flow",
        postanes_bank_utils
        .format_currency(
            result[
                "net_cash_flow"
            ]
        )
    )

    st.divider()
    
    # ANALYSIS 3
    # SPENDING INSIGHTS (NEW THINGY)
    
    st.subheader("2. Spending Insights (Charts)")

    flow_data = pd.DataFrame({
        "Type": ["Deposits", "Withdrawals"],
        "Amount": [result["total_deposited"], result["total_withdrawn"]]
    })

    # Bar chart
    st.bar_chart(flow_data.set_index("Type"))

    # Pie chart
    fig, ax = plt.subplots()
    ax.pie(
        flow_data["Amount"],
        labels=flow_data["Type"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["#50DF87", "#D55A52"],
        textprops={
            'fontsize': 13, 
            'fontweight': 'bold'
            }
    )
    ax.axis("equal")
    st.pyplot(fig)

    st.divider()
    
    

    # ==================================
    # ANALYSIS 4
    # ACCOUNT ACTIVITY
    # ==================================

    st.subheader(
        "3. Account Activity Analysis"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Largest Transaction",
        postanes_bank_utils
        .format_currency(
            result[
                "largest_transaction"
            ]
        )
    )

    col2.metric(
        "Average Transaction",
        postanes_bank_utils
        .format_currency(
            result[
                "average_transaction"
            ]
        )
    )

    col3.metric(
        "Latest Transaction",
        result[
            "latest_transaction"
        ]
    )

    st.caption(
        f"Latest Activity: "
        f"{result['latest_timestamp']}"
    )

# PAY BILLS (NEW THING)

def bills_page():
    account = st.session_state.account
    st.header("Bills Payment")

    st.write(
        f"Available Balance: **{postanes_bank_utils.format_currency(account.check_balance())}**"
    )

    # BILL CATEGORIES
    bill_type = st.selectbox(
        "Select Bill Type",
        ["Electricity", "Water", "Internet", "Tuition", "Other"]
    )

    amount = st.number_input(
        "Payment Amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button(
        "Pay Bill",
        type="primary",
        icon="📑",
        use_container_width=True
    ):
        if amount > account.check_balance():
            st.error("Insufficient balance for this payment.")
            return

        success = account.withdraw(amount)

        if success:
            postanes_bank_storage.update_account(account)
            postanes_bank_transactions.record_transaction(
                account,
                f"Bill Payment - {bill_type}",
                amount
            )
            st.success(f"Payment for {bill_type} successful.")
            st.metric("New Balance", postanes_bank_utils.format_currency(account.check_balance()))
        else:
            st.error("Payment failed.")


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "account" not in st.session_state:

    st.session_state.account = None


# ==========================================
# BANK HEADER
# ==========================================

st.title("Postanes BANK")

st.caption(
    "Secure Digital Banking System"
)


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        [
            "Login",
            "Register"
        ]
    )


    # ======================================
    # LOGIN
    # ======================================

    with login_tab:

        st.subheader(
            "Welcome Back"
        )

        account_number = st.text_input(
            "Account Number",
            key="login_account"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="login_pin"
        )

        if st.button(
            "Login",
            type="primary",
            icon="🔑",
            use_container_width=True
        ):

            account, message = (
                postanes_bank_auth
                .login_account(
                    account_number,
                    pin
                )
            )

            if account is not None:

                st.session_state.logged_in = True

                st.session_state.account = (
                    account
                )

                st.success(message)

                st.rerun()

            else:

                st.error(message)


    # ======================================
    # REGISTRATION
    # ======================================

    with register_tab:

        st.subheader(
            "Create Your Postanes Bank Account"
        )

        name = st.text_input(
            "Full Name",
            key="register_name"
        )

        account_number = st.text_input(
            "Account Number",
            key="register_account"
        )

        pin = st.text_input(
            "Create 4-Digit PIN",
            type="password",
            key="register_pin"
        )

        confirm_pin = st.text_input(
            "Confirm PIN",
            type="password",
            key="register_confirm_pin"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Savings Account",
                "Student Account"
            ]
        )

        starting_balance = st.number_input(
            "Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button(
            "Create Account",
            type="primary",
            icon="📝",
            use_container_width=True
        ):

            account, message = (
                postanes_bank_auth
                .register_account(
                    name,
                    account_number,
                    pin,
                    confirm_pin,
                    account_type,
                    starting_balance
                )
            )

            if account is not None:

                st.success(message)

                st.info(
                    "Your account has been created. "
                    "Please use the Login tab."
                )

            else:

                st.error(message)


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )

    # ======================================
    # PAGE REGISTRY
    # ======================================
    # (function, title, icon) for every page.
    # Used to build both the st.Page objects
    # for routing and the st.page_link rows
    # below, so the two can never drift out
    # of sync with each other.

    page_defs = [
        (dashboard_page, "Dashboard", "🏠"),
        (deposit_page, "Deposit", "💰"),
        (withdraw_page, "Withdraw", "💸"),
        (history_page, "Transaction History", "📜"),
        (analysis_page, "Transaction Analysis", "📊"),
        (goals_page, "Savings Goals!", "🎯"),
        (bills_page, "Pay Bills", "📑"),
    ]

    pages = [
        st.Page(func, title=title, icon=icon)
        for func, title, icon in page_defs
    ]

    # position="hidden" turns off Streamlit's
    # built-in nav widget (which always forces
    # itself to the very top of the sidebar) so
    # our branding/profile block above can stay
    # where it is, while st.navigation still
    # handles routing and st.page_link below
    # still gets the automatic active-page
    # highlight.
    pg = st.navigation(
        pages,
        position="hidden"
    )


    # ======================================
    # SIDEBAR
    # ======================================

    st.sidebar.title(
        "Postanes BANK"
    )

    st.sidebar.write(
        f"**{account.account_name}**"
    )

    st.sidebar.caption(
        account.get_account_type()
    )

    st.sidebar.write(
        f"Account: "
        f"{account.account_number}"
    )

    st.sidebar.divider()


    st.sidebar.caption(
        "BANKING MENU"
    )

    for page, (func, title, icon) in zip(
        pages,
        page_defs
    ):

        st.sidebar.page_link(
            page,
            label=title,
            icon=icon,
            use_container_width=True
        )


    st.sidebar.divider()


    if st.sidebar.button(
        "Logout",
        type="secondary",
        icon="🚪",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.rerun()


    # ======================================
    # RUN THE SELECTED PAGE
    # ======================================

    pg.run()


# """
######### Learning Signature #########
# Programmed by: Mary Julia Gabrielle E. Postanes
# Date Submitted: September 13, 2026

# Program Description: This program shows the full working Bank application.
# Reflection: I learned that editing some stuff can further improve thr program.

# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [/] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner﻿ – Used AI to design, structure, or co-create significant code.
# """

# AI USE: I useed AI for explanations, examples, as well as some ideas on areas I need to improve on.