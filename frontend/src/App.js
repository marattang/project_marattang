import React from 'react'
import {Route, Redirect} from "react-router-dom"
import {Login, SignUp, UserDetail, UserEdit, UserList} from 'user/components'
import {Home, User, Counter, Item, Article, Todo} from 'templates'
import {Nav} from 'common'
import { BrowserRouter as Router} from 'react-router-dom'
import {todoReducer} from 'store'
import {createStore, combineReducers} from 'redux'
import {Provider} from 'react-redux'
import {ItemList, ItemDetail, ItemRegister, ItemModify} from 'item/components'
import {ArticleDetail, ArticleFrom, ArticleWrite, ArticleModify} from 'article/components'
import {TodoInput, TodoList} from 'todos/components'
import {Schedule} from 'todos/containers'

const rootReducer = combineReducers({todoReducer})


const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/counter' component={Counter}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/item' component={Item}/>
        <Route exact path='/article' component={Article}/>
        <Route exact path='/todo' component={Todo}/>

        <Route exact path='/login-form' component={Login}/>
        <Route exact path='/signup-form' component={SignUp}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-Edit' component={UserEdit}/>
        <Route exact path='/user-List' component={UserList}/>

        <Route exact path='/item-list' component={ItemList}/>
        <Route exact path='/item-detail' component={ItemDetail}/>
        <Route exact path='/item-modify' component={ItemModify}/>
        <Route exact path='/item-register' component={ItemRegister}/>

        <Route exact path='/article-detail' component={ArticleDetail}/>
        <Route exact path='/article-modify' component={ArticleModify}/>
        <Route exact path='/article-write' component={ArticleWrite}/>
        <Route exact path='/article-from' component={ArticleFrom}/>
        
        <Route exact path='/todo-input' component={TodoInput}/>
        <Route exact path='/todo-list' component={TodoList}/>
        
        {/* <Route exact path='/todo_work' component={Schedule}/> */}

      </Provider>
    </Router>
  </div>)
}
export default App