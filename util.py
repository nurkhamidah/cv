import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import re

# --------------------------- COLORS
red = '#ff4c50'
black = '#272829'
brown1 = '#985646'
brown2 = '#bf8859'
brown3 = '#9c7d61'
brown4 = '#b9735c'
green1 = '#4f746c'
green2 = '#79a99d'
green3 = '#6d7961'
blue1 = '#4b7784'
blue2 = '#6ca2af'
blue3 = '#a9bcc2'
nude1 = '#9be7e78'
nude2 = '#c3b4af'
nude3 = '#ada08d'

# --------------------------- DATA
experience = pd.read_excel('data/Tableau CV-2.xlsx', sheet_name='EXPERIENCE')
skill = pd.read_excel('data/Tableau CV-2.xlsx', sheet_name='SKILL')
language = pd.read_excel('data/Tableau CV-2.xlsx', sheet_name='LANGUAGES')
certification = pd.read_excel('data/Tableau CV-2.xlsx', sheet_name='CERTIFICATION')
portfolio = pd.read_excel('data/Tableau CV-2.xlsx', sheet_name='PORTFOLIO')

# --------------------------- FUNCTIONS
def stringSplit(strs):
    return(re.split(",", strs))

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

# --------------------------- TABLE
experience['Association'] = experience['Association'].apply(stringSplit)
experience['Tools'] = experience['Tools'].apply(stringSplit)
experience['Hard Skill'] = experience['Hard Skill'].apply(stringSplit)
experience['Soft Skill'] = experience['Soft Skill'].apply(stringSplit)
skill['Associated with'] = skill['Associated with'].apply(stringSplit)
portfolio['Skill'] = portfolio['Skill'].apply(stringSplit)
portfolio['Method'] = portfolio['Method'].apply(stringSplit)
portfolio['Tools'] = portfolio['Tools'].apply(stringSplit)
portfolio['Date'] = portfolio['Date'].apply(lambda x: x.strftime('%B %d, %Y'))
experience['Duration (Month)'] = experience.apply(lambda x: diff_month(x['End'], x['Start']),
                                                  axis=1)

# --------------------------- UTILITIES

# --------------------------- About
## ------------------------------------- TXT
about = '<div class="txt"><b>Data Scientist</b> with a strong foundation in statistical modeling, machine learning, and data visualization. Proven expertise in <b>Python, R, SQL, and NoSQL databases</b>, with a track record of developing innovative solutions and insightful analytics. Adept at handling large datasets, conducting comprehensive research, and delivering actionable insights. Seeking to leverage my skills and experience to contribute to cutting-edge projects in data science and analytics. Some of the analytical techniques mastered include statistical modeling, analysis of unstructured data such as text data, machine learning including clustering and classification and their anomaly handling and interpretation, and deep learning with BERT.</div>'

# --------------------------- Experience
## ------------------------------------- GANTT CHART
df_exp = []
for i in range(len(experience)):
    df_exp.append(dict(
        Task = experience.loc[i, 'Position'],
        Start = str(experience.loc[i, 'Start']),
        Finish = str(experience.loc[i, 'End']),
        Resource = experience.loc[i, 'Type'],
        Description = experience.loc[i, 'Organization']
    ))

colors = {'Education': brown1,
          'Work': brown2,
          'Course': blue1,
          'Organization': brown3,
          'Activity': green3,
          'Lecture': blue2}

gc = ff.create_gantt(df_exp, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True, showgrid_x=True, showgrid_y=True)
gc.update_layout(autosize=True, title='', title_x=0.5)

## ------------------------------------- BAR CHART
def makeBarchart(df, col1, col2):
    df = df.groupby([col1])[col2].sum()
    fig = px.bar(df)
    # Customize labels
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return(fig)

def makeBarChart2(types, expr, yoe):
    bar_yoe = go.Bar(name='YoE', x=skill[skill['Type'] == types]['Name'], 
                y=skill['Years of Experience'], yaxis='y2', offsetgroup=2, marker_color='darkSlateGrey',
                customdata=skill[skill['Type'] == types][['First Use', 'Latest Use', 'Type', 'Associated with']],
                hovertemplate='''<b>%{customdata[2]}: </b>%{x} with usage %{y} year(s)<br><b>First Usage: </b>%{customdata[0]}<br><b>Association: </b>%{customdata[3]}''')
    bar_lev = go.Bar(name='Level', x=skill[skill['Type'] == types]['Name'], 
                y=skill['Expertise Level (out of 5)'], yaxis='y', offsetgroup=1, marker_color='grey',
                customdata=skill[skill['Type'] == types][['First Use', 'Latest Use', 'Type', 'Associated with']],
                hovertemplate='''<b>%{customdata[2]}: </b> %{x} with expertise %{y} out of 5<br><b>First Usage: </b>%{customdata[0]}<br><b>Association: </b>%{customdata[3]}''')
    fig = go.Figure()
    if expr:
        fig.add_trace(bar_lev)
        fig.update_layout({'yaxis': {'title': 'Expertise Level (out of 5)'}}, barmode='group')
    if yoe:
        fig.add_trace(bar_yoe)
        fig.update_layout({'yaxis2':{'title': 'Years of Experienced', 'overlaying': 'y', 'side': 'right'}}, barmode='group')
    return fig

