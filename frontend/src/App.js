import React from 'react'
import { BrowserRouter as Router, Link } from "react-router-dom"
import styled from 'styled-components';
import Counter from './counter/Counter'
import Login from './user/Login'
import SignUp from './user/SignUp'
import UserDetail from './user/UserDetail'
import UserEdit from './user/UserEdit'
import UserList from './user/UserList'

const App = () => {
  return(
    <Container>
    <Element>
  </Element>
  </Container>)
}
const Container = styled.div`
    width: 100%,
    border: 1px solid #d1d8e4;
s`
const Element = styled.div`
    width: 400px;
    margin: 0 auto;
`
export default App