import streamlit as st

from binary_search import BinarySearch

tab1, tab2, tab3 = st.tabs(["二分查找", "Dog", "Owl"])

with tab1:
    b_search = BinarySearch()
    b_search.frontpage()
