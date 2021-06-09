import React from 'react'
import {TodoInput, TodoList} from '../components/index'
import {Provider} from 'react-redux'
import {store} from '../store/index'

const Schedule = () => {
    return(
        <>
        <Provider store={store}>
            <TodoInput/>
            <TodoList/>
        </Provider>
        </>
    )
}
export default Schedule