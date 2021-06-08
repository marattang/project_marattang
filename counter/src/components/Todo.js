import React, { useState } from 'react'

const Todo = () => {

    const [item, setItem] = useState('')

    return(<>
        <h1>할일 목록</h1>
        <h4>{item}</h4>
        <input onChange = {e => setItem(e.target.value)}/> <br/>
        <button onClick = {() => setItem('')}>할일 삭제</button>
    </>)
}
export default Todo