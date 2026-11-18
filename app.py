import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SupeRR Selector | Pressure Analytics", page_icon="🏏", layout="wide")
bat = pd.read_csv("corrected_top_batters.csv")
bowl = pd.read_csv("corrected_top_bowlers.csv")

st.title("🏏 SupeRR Selector Season 2")
st.subheader("Pressure Performance Analytics")
st.caption("Audited primary rankings | IPL and T20I | Pressure index ≥ 60")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Matches analysed","837")
c2.metric("Deliveries analysed","193,988")
c3.metric("High-pressure deliveries","21,817")
c4.metric("Primary pressure threshold","60 / 100")

tab1,tab2,tab3 = st.tabs(["Overview","Batting","Bowling"])
with tab1:
    left,right=st.columns(2)
    with left:
        st.markdown("### Top 10 Batters")
        st.dataframe(bat[["Rank","Player","Pressure Score","Pressure Balls","Pressure Matches"]],hide_index=True,use_container_width=True)
    with right:
        st.markdown("### Top 10 Bowlers")
        st.dataframe(bowl[["Rank","Player","Pressure Score","Pressure Legal Balls","Wickets","Pressure Matches"]],hide_index=True,use_container_width=True)
with tab2:
    st.markdown("### Batting leaderboard")
    st.plotly_chart(px.bar(bat.sort_values("Pressure Score"),x="Pressure Score",y="Player",orientation="h",title="Audited batting pressure score"),use_container_width=True)
    player=st.selectbox("Inspect batter",bat["Player"].tolist())
    r=bat[bat.Player==player].iloc[0]
    a,b,c=st.columns(3)
    a.metric("Pressure strike rate",f'{r["Pressure SR"]:.2f}')
    b.metric("Normal strike rate",f'{r["Normal SR"]:.2f}')
    c.metric("Pressure balls",int(r["Pressure Balls"]))
with tab3:
    st.markdown("### Bowling leaderboard")
    st.plotly_chart(px.bar(bowl.sort_values("Pressure Score"),x="Pressure Score",y="Player",orientation="h",title="Audited bowling pressure score"),use_container_width=True)
    player=st.selectbox("Inspect bowler",bowl["Player"].tolist())
    r=bowl[bowl.Player==player].iloc[0]
    a,b,c=st.columns(3)
    a.metric("Pressure economy",f'{r["Pressure Economy"]:.2f}')
    b.metric("Normal economy",f'{r["Normal Economy"]:.2f}')
    c.metric("Pressure wickets",int(r["Wickets"]))
st.divider()
st.caption("Scores are relative composite indices under the published methodology, not probabilities. Rankings are sensitive to model assumptions; see the accompanying methodology report.")
