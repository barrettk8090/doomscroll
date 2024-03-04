import {Link} from 'react-router-dom'

function Home(){
    // const { data: { user } } = await supabase.auth.getUser()
    // console.log(getSession().session.user)

    return (
        <div>
            <div className="mt-60">
                <h1 className="font-display text-9xl">DOOMSCROLL</h1>
                <div className="mx-48">
                    <p className="my-12 font-type text-5xl">Your politics-free feed for keeping up-to-date on the end of the world.</p>
                </div>
                <Link to="/create-account"><button className="mx-4 text-2xl">Create Account</button></Link>
                <Link to="/login"><button className="mx-4 text-2xl">Log In</button></Link>
            </div>
            <p className="mt-64 font-type font-bold text-3xl"> Making conspiracies fun again. Read our ethos.</p>
        </div> 
    )
}

export default Home