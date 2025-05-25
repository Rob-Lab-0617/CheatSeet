import streamlit as st

icon='https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg'

st.set_page_config(
  page_title='Markdown CheatSheet'
  page_icon=icon,
  layout='wide'
)

st.logo(icon,link='https://github.github.com/gfm/')
st.markdown('### Markdown チートシード')

left,right = st.columns(2)

left.markdown('**:memo: テキスト書式')
left.markdown('''
  
)
