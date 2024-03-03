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

function App() {
  

  return (
    
    <>

      <BrowserRouter>
        {/* <Nav user={user} setUser={setUser} ethAddress={ethAddress} setEthAddress={setEthAddress} connectWallet={connectWallet}/> */}
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/feed" element={<FeedMain supabase={supabase}/>} />

        </Routes>
        </BrowserRouter>
      </>
  )
}

export default App
