import React from 'react'
import './App.css';
import {Counter} from "./components/index"
import {Route} from 'react-router-dom'

const App = () => {
  return (
    <div className="App">
      <Route exactpath='/' component={Counter}/>
    </div>
  );
}

export default App;
