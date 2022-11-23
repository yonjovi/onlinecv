import streamlit as st
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Yon Rotem")
col1, col2 = st.columns([2, 40])
with col1:
    st.markdown("[![Linkedin](https://i.ibb.co/dc9fNT5/linkedin24.png)](https://Linkedin.com/in/yonrotem)", unsafe_allow_html=True)
with col2:
    st.markdown("[![Github](https://i.ibb.co/KqkzgpS/github24.png)](https://github.com/yonjovi)", unsafe_allow_html=True)



st.header("a finance specialist, programmer, creator")

st.info("Scroll right for more 👉👉")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["CAREER PROFILE", "AREAS OF EXPERTISE", "SYSTEMS & APPLICATIONS", "CERTIFICATIONS & TRAINING", "CAREER", "📞"])

with tab1:
    st.subheader("CAREER PROFILE")
    st.write(
        "A proactive and knowledgeable Financial Services and Client Services Management professional with extensive "
        "experience and track record in achieving great results and providing outstanding client and business "
        "support. I provide exceptional analysis and problem solving capabilities to deliver innovative solutions "
        "that align with business strategies and goals.")

with tab2:
    st.subheader("AREAS OF EXPERTISE")
    st.markdown(
        "- Managing client financial needs and providing service to ensure client satisfaction through accurate "
        "and consistent reporting delivered in client review meetings.")
    st.markdown(
        "- Using my financial services and data analytics expertise to provide accurate and exquisite reporting "
        "to evaluate client needs, objectives, and solutions.")
    st.markdown(
        "- Working with and leading a client services team to establish consistency, meet deadlines and achieve excellent results.")
    st.markdown(
        "- Writing compliant advice documents and presenting advice to clients while supporting a lead adviser and playing an integral part in client onboarding processes.")
    st.markdown("- Implementing advice and executing trade orders in accordance with the advice provided to clients.")
    st.markdown(
        "- Evaluating, configuring, developing and deploying new strategies, using new system, software, and products to offer competitive solutions to the practice and its clients.")
    st.markdown(
        "- Keeping the business up to date with a fast-paced and changing financial services regulatory and compliance environment, leading to exceptional audit results.")
    st.markdown(
        "- Transferring financial and I.T knowledge back into business support functions as projects transition to completion.")

with tab3:

    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("SYSTEMS & APPLICATIONS")

        st.write("🐍 Python - Advanced Skills")
        st.write("💾 R - Intermediate Skills")
        st.write("👾 JavaScript - Intermediate Skills")
        st.write("💼 HTML & CSS - Intermediate Skills")
        st.write("🎒 Microsoft Power Tools - Intermediate Skills")
        st.write("💻 Microsoft Office Suite - Advanced Skills")
        st.write("🧑‍🎨 Adobe Suite - Intermediate Skills")
        st.write("🧮 XPLAN - Advanced Skills")

    with col2:
        st.subheader("LANGUAGES")
        st.write("🇦🇺 English - Fluent")
        st.write("🇮🇱 Hebrew - Fluent")

with tab4:
    with st.container():
        st.subheader("CERTIFICATIONS & TRAINING")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("##### Course")

        with col2:
            st.markdown("##### Institute")

        with col3:
            st.markdown("##### Year Completed")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Foundations of Cyber Security")

        with col2:
            st.write("CyberCX & CompTIA")

        with col3:
            st.write("2022 (Current)")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("100 Days of Coding")

        with col2:
            st.write("Angela Yu")

        with col3:
            st.write("2022")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Graduate of Data Analytics")

        with col2:
            st.write("Deakin University")

        with col3:
            st.write("2021")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Diploma of Financial Planning")

        with col2:
            st.write("Kaplan Professional")

        with col3:
            st.write("2016")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Bachelor of Business")

        with col2:
            st.write("Monash University")

        with col3:
            st.write("2012")

with tab5:
    with st.container():
        st.subheader("CAREER")
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("#### Role")
            with col2:
                st.markdown("#### Organisation")
            with col3:
                st.markdown("#### Year")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Client Services Manager")
            with col2:
                st.write("Calibre Private Wealth Advisers")
            with col3:
                st.write("2021 - Current")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Associate Adviser")
            with col2:
                st.write("Maddern Financial Advisers")
            with col3:
                st.write("2020 - 2021")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Client Services Manager")
            with col2:
                st.write("Portfolio Planners")
            with col3:
                st.write("2020")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Services Team")
            with col2:
                st.write("Generation Life")
            with col3:
                st.write("2019 - 2020")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Client Services")
            with col2:
                st.write("Taylors Accountants & Advisors")
            with col3:
                st.write("2010 - 2019")

        st.write("")

        st.subheader("Achievements")

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("###### Client Services Manager")
            with col2:
                st.markdown("###### Calibre Private Wealth Advisers")
            with col3:
                st.markdown("###### 2021 - Current")
            st.write("")
            st.markdown("- Responsible great audit results for which our firm received the highest audit score to date.")
            st.markdown(
                "- Implemented new ASIC regulations for Ongoing Service Agreements with 100% accuracy.")
            st.markdown("- Produced accurate and descriptive reports for all client review meetings and implemented advice left "
                     "over from previous employees.")
            st.markdown(
                "- Assisted clients receive financial remediation from National Australia Bank (NAB).")
            st.write("")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("###### Associate Adviser")
            with col2:
                st.markdown("###### Maddern Financial Advisers")
            with col3:
                st.markdown("###### 2020 - 2021")
            st.write("")
            st.markdown(
                "- Managing 170 clients and ensuring client satisfaction through accurate and consistent reporting delivered in client review meetings.")
            st.markdown(
                "- Managed a difficult insurance claims for our biggest clients, and assisting clients with financials hardships keep during the COVID-19 pandemic, including early release of superannuation.")
            st.markdown("- Placing and executing all trades for clients.")
            st.markdown(
                "- Acting as the only Associate Adviser and Client Services Manager for 3 months and meeting all deadlines and compliance requirements.")
            st.write("")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("###### Client Services Manager")
            with col2:
                st.markdown("###### Portfolio Planners")
            with col3:
                st.markdown("###### 2020")
            st.write("")
            st.markdown("- Successfully managing the administration team and meeting deadlines with high quality results.")
            st.markdown("- Completing the rollovers for our entire client base to our newly preferred platform.")
            st.markdown(
                "- Helping clients access funds and protect their wealth during market volatility in the beginning of the COVID-19 pandemic.")
            st.write("")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("###### Services Team")
            with col2:
                st.markdown("###### Generation Life")
            with col3:
                st.markdown("###### 2019 - 2020")
            st.write("")
            st.markdown("- Managed to process the largest amount of applications per day in record time and accuracy rates.")
            st.markdown(
                "- Responsible along with the rest of the services team for a successful growth period for the business for which the Responsible along with the rest of the services team for a successful growth period for the business for which the business received reports for excellence.")
            st.markdown("- Received a promotion for my dedication and hard work.")
            st.write("")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("###### Client Services")
            with col2:
                st.markdown("###### Taylors Accountants & Advisors")
            with col3:
                st.markdown("###### 2010 - 2019")
            st.write("")
            st.markdown("- Achieved full-time employment during the completion of my tertiary education..")
            st.markdown("- Promotion to Client Services Manager during my employment.")
            st.markdown(
                "- Providing support to the lead adviser and involvement in producing, presenting, and implementing all client advice.")
            st.markdown(
                "- Successfully managed to restore our server’s data from a backup without losing any files, after being the firm fell victim to a cyber-attack which held all client data for ransom.")

with tab6:
    st.subheader("CONTACT ME")
    st.write("📱 0422 815 384")
    st.write("💬 rotemyon@gmail.com")

