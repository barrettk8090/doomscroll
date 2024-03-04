import React from "react";
import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"

function Login({supabase}){

    const [userEmail, setUserEmail] = useState("")
    const [password, setPassword] = useState("")

    const loginUser = async (e) => {
        e.preventDefault();
        const { data, error } = await supabase.auth.signInWithPassword({
            email: userEmail,
            password: password,
          })
        console.log(data)
        //Need to add "if user --> validation"
        navigate('/feed')
    }

    const navigate = useNavigate()

    return(
        <>
            <form>
                <label>Email </label>
                <input type="text" id="email" name="email" value={userEmail} onChange={(e) => setUserEmail(e.target.value)}/>

                <label>Password </label>
                <input type="text" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>

                <button type="submit" onClick={(loginUser)}>Login</button>
            </form>
        </>
    )


}

export default Login