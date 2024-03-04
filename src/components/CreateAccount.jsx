import { useState, useEffect } from "react"

function CreateAccount({supabase}){

    const [userEmail, setUserEmail] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")


    const createUser = async (e) => {
        e.preventDefault();
        const { data, error } = await supabase.auth.signUp({
            email: userEmail,
            password: password,
            })   
    }



    return(
        <>
            <div>
                <h1 className="font-type text-6xl"> Create Your Account</h1>
                <p className="font-type text-3xl">An account is required to view and subscribe to feed topics and create your custom doomscroll feed. </p>
            </div>

            <form>
                <label htmlFor="email">Email Address </label>
                <input type="text" id="email" name="email" value={userEmail} onChange={(e) => setUserEmail(e.target.value)}/>

                <label htmlFor="username">Username </label>
                <input type="text" id="username" name="username" value={username} onChange={(e) => setUsername(e.target.value)}/>

                <label htmlFor="password">Password </label>
                <input type="text" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>

                <button type="submit" onClick={createUser}>Create Account</button>
            </form>
        </>
    )
}

export default CreateAccount