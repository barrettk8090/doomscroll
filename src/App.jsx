import { useState, useEffect } from 'react'
import {
  createBrowserRouter,
  BrowserRouter,
  RouterProvider,
  Routes,
  Route,
  Router,
  Link
} from "react-router-dom";

import supabase from './Config/supabaseClient'

import './App.css'
import Home from './components/Home'
import FeedMain from './components/FeedMain'
import CreateAccount from './components/CreateAccount';
import Login from './components/Login'

function App() {
  

  return (
    
    <>

      <BrowserRouter>
        {/* <Nav user={user} setUser={setUser} ethAddress={ethAddress} setEthAddress={setEthAddress} connectWallet={connectWallet}/> */}
        <nav>
          <ul className="flex justify-between">
            <Link to="/"><li>Home</li></Link>
            <Link to="/create-account"><li>Create Account</li></Link>
            <Link to="login"><li>Login</li></Link>
            <Link to="/feed"><li>Feed Main</li></Link>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/feed" element={<FeedMain supabase={supabase}/>} />
          <Route path="/create-account" element={<CreateAccount supabase={supabase} />}/>
          <Route path="/login" element={<Login supabase={supabase}/>} /> 

        </Routes>
        </BrowserRouter>
      </>
  )
}

export default App
