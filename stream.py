import streamlit as st
from streamlit_option_menu import option_menu
from data import *

st.set_page_config(
    page_title="Nur Khamidah",
    page_icon="💖",
    layout='wide',
)

with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown('<h1>NUR <b>KHAMIDAH</b></h1>', unsafe_allow_html=True)

pages = option_menu("", ['About', 'Experiences', 'Skills & Portfolios', 'Certificates'], 
    icons=['file-person', 'send-arrow-up', 'bag-fill', 'file-earmark-text', 'chat-left-quote'], default_index=0, orientation="horizontal")

# --------------------------- About
if pages == 'About':
    ab1, ab2, ab3, ab4, ab5, ab6, ab7 = st.columns([1, 5, 1, 4, 1, 5, 1])
    with ab2:
        st.markdown('<h2>ABOUT <b>ME</b></h2>', unsafe_allow_html=True)
        st.markdown(about, unsafe_allow_html=True)
        
    with ab4:
        " "
        " "
        " "
        st.image('data/img_cv.png')
    
    with ab6:
        " "
        " "
        
        st.markdown('<div class="txt2"><b>Nur Khamidah, S.Stat.</b></div>', unsafe_allow_html=True)
        st.markdown('<div class="txt2">Bogor Indonesia 16116</div>', unsafe_allow_html=True)
        " "
        with st.container():
            st.markdown('<h2>LINKS</h2>', unsafe_allow_html=True)
            con1, con1b, con2, con2b, con3, con3b, con4 = st.columns([3,1,3,1,3,1,3])
            with con1:
                st.image('data/img_li.png', use_column_width=True)
                st.page_link(page='https://linkedin.com/in/nurkhamidah', label='LinkedIn')
            with con2:
                st.image('data/img_gh.png', use_column_width=True)
                st.page_link(page='https://github.com/nurkhamidah', label='GitHub')
            with con3:
                st.image('data/img_r.png', use_column_width=True)
                st.page_link(page='https://rpubs.com/nurkhamidah', label='RPubs')
            with con4:
                st.image('data/img_rg.png', use_column_width=True)
                st.page_link(page='https://www.researchgate.net/profile/Nur-Khamidah-3', label='ResearchGate')
                
        " "        
        st.markdown('<div class="txt2">See another version of this CV</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.page_link(page='https://bit.ly/tableau_nurkhamidah', label='TABLEAU VER', icon='🔗', use_container_width=True)
            st.download_button(label='⬇️ DOWNLOAD CV', data = 'data/Nur    Khamidah_CV_2.pdf', file_name='CV Nur Khamidah.pdf')
        
# --------------------------- Experiences
if pages == 'Experiences':
    st.markdown('<h2>OVERALL <b>EXPERIENCES</b></h2>', unsafe_allow_html=True)
    st.plotly_chart(gc)
    
    st.markdown('<h2>DURATION OF <b>EXPERIENCES</b></h2>', unsafe_allow_html=True)
    exp1, exp2 = st.columns([1,5])
    with exp1:
        base_exp = st.selectbox('Show Based on:', ['Organization', 'Position'])
        base_skill = st.checkbox('Filter based on tools/skills')
        if base_skill:
            skill_exp = st.selectbox('Choose tools/skills:', ['Tools', 'Hard Skill', 'Soft Skill'])
            skill_opt = st.multiselect('Choose '+ skill_exp, set(experience[skill_exp].explode().to_list()))
            experience = experience[[any(x in i for x in skill_opt) for i in experience[skill_exp]]]
    with exp2:
        st.plotly_chart(makeBarchart(experience, base_exp, 'Duration (Month)'))
         
    st.markdown('<h2>DETAIL <b>EXPERIENCES</b></h2>', unsafe_allow_html=True)
            
    exp3, exp4, exp5 = st.columns([1,1,1])
    with exp3:
        exp_name = st.selectbox('Choose Position:', experience['Position'].unique())
    with exp4:
        exp_org = st.selectbox('Choose Organization:', experience[experience['Position'] == exp_name]['Organization'].unique())
        
    exp6, exp7, exp8 = st.columns([1,1,2], gap='medium')
    dat_exp = experience[experience['Position'] == exp_name][experience['Organization'] == exp_org].reset_index()
    with exp6:
        st.markdown('<div class="txt"><b>Experience: </b>{} at {}</div>'.format(dat_exp['Position'][0], dat_exp['Organization'][0]), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Time: </b>{} to {}</div>'.format(dat_exp['Start'].apply(lambda x: x.strftime('%B %Y'))[0], dat_exp['End'].apply(lambda x: x.strftime('%B %Y'))[0]), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Location: </b>{}, {}</div>'.format(dat_exp['City '][0], dat_exp['State'][0]), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Duration: </b>{} years and {} months</div>'.format(dat_exp['Duration (Month)'][0] // 12, dat_exp['Duration (Month)'][0] % 12), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Associated with: </b>{}</div>'.format(', '.join(dat_exp['Association'][0])), unsafe_allow_html=True)
    with exp7:
        st.markdown('<div class="txt"><b>Tools used: </b>{}</div>'.format(', '.join(dat_exp['Tools'][0])), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Hard skills used: </b>{}</div>'.format(', '.join(dat_exp['Hard Skill'][0])), unsafe_allow_html=True)
        st.markdown('<div class="txt"><b>Soft skills used: </b>{}</div>'.format(', '.join(dat_exp['Soft Skill'][0])), unsafe_allow_html=True)
    with exp8:
        st.markdown('<div class="txt"><b>Description </b>{}</div>'.format(dat_exp['Description'][0].replace('\n', '<br>')), unsafe_allow_html=True)
    
# --------------------------- Skills & Portfolios
if pages == 'Skills & Portfolios':
    st.markdown('<h2>PORTFOLIOS<b></b></h2>', unsafe_allow_html=True)
    por1, por2 = st.columns([1,4], gap='large')
    with por1:
        por_opt = st.selectbox('Filter by', ['All', 'Type', 'Skill', 'Tools', 'Method', 'Status'])
        if por_opt == 'All':
            dat_por = portfolio[['Name', 'Link', 'Date', 'Type', 'Tools', 'Method', 'Associated with', 'Status']]
        elif por_opt in ['Type', 'Status']:
            por_opt2 = st.multiselect('Select '+ por_opt, portfolio[por_opt].unique())
            dat_por = portfolio[portfolio[por_opt].isin(por_opt2)][['Name', 'Link', 'Date', 'Type', 'Tools', 'Method', 'Associated with', 'Status']]
        else:
            por_opt2 = st.multiselect('Select '+ por_opt, set(portfolio[por_opt].explode().to_list()))
            dat_por = portfolio[[any(x in i for x in por_opt2) for i in portfolio[por_opt]]][['Name', 'Link', 'Date', 'Type', 'Tools', 'Method', 'Associated with', 'Status']]
    with por2:
        st.dataframe(dat_por, use_container_width=True, hide_index=True,
                     column_config = {
                         "Link": st.column_config.LinkColumn('Link'),
                         "Tools" : st.column_config.ListColumn('Tools'),
                         "Method" : st.column_config.ListColumn('Method')
                     })
    st.markdown('<h2>SKILL <b>PRACTICED</b></h2>', unsafe_allow_html=True)
    ski1, ski2, ski3 = st.columns([1,1,3], gap='large')
    with ski2:
        '**Show bar based on:**'
        ski_exp = st.checkbox('Expertise Level', value=True)
        ski_yoe = st.checkbox('YoE', value=True)
    with ski1:
        ski_opt = st.selectbox('Choose type of skill:', skill['Type'].unique())
    st.plotly_chart(makeBarChart2(ski_opt, ski_exp, ski_yoe))
    
# --------------------------- Certificates
if pages == 'Certificates':
    st.markdown('<h2>COURSE <b>CERTIFICATES</b></h2>', unsafe_allow_html=True)
    st.dataframe(certification, use_container_width=True)
    
    st.markdown('<h2>PREFERRED <b>LANGUAGES</b></h2>', unsafe_allow_html=True)
    st.dataframe(language, use_container_width=True)

    