import streamlit as st
from issues import generate_random_issue

#STREAMLIT PAGE SETUP
st.set_page_config(page_title='Help Desk Ticket Simulator',layout="centered")
st.title('Help Desk Ticket System Simulator')
st.info('Generate a random support ticket, then see the recommended fix.')

# SESSION STATE ISSUE STORING
if "current_issue" not in st.session_state:
    st.session_state.current_issue = None

# CLICKABLE BUTTON TO GENERATE ISSUES
if st.button('Click to generate'):
    st.session_state.current_issue = generate_random_issue()

    st.write('Generating Issue...')

    st.success('Issue detected')

# SHOW ISSUE DESCRIPTION AND RECOMMENDED FIX
if st.session_state.current_issue:
    issue = st.session_state.current_issue
    with st.container(border=True):
        st.subheader(f"🎫 {issue['title']}")
        st.markdown(f"**Description:** {issue['description']}")
        st.markdown("**Recommended Fix Command:**")
        st.code(issue["fix_command"], language="bash")

        # Optional: Add a "Simulate Fix" button
        if st.button("🧑‍💻 Run Fix Simulation"):
            st.success(f"✅ {issue['fix_command']} executed successfully (simulated)")