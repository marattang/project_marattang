import React from 'react'
import {Route, withRouter} from "react-router-dom"
import {Counter} from 'counter/index'
import {Login, SignUp, UserDetail, UserEdit, UserList} from 'user/index'
import {Home} from 'common/index'


const App = () => {
  return (<div>
      <Route exact path='/' component={Home}/>
      <Route exact path='/counter' component={Counter}/>
      <Route exact path='/login' component={Login}/>
      <Route exact path='/signUp' component={SignUp}/>
      <Route exact path='/user-detail' component={UserDetail}/>
      <Route exact path='/user-Edit' component={UserEdit}/>
      <Route exact path='/user-List' component={UserList}/>
  </div>)
}
export default withRouter(App)