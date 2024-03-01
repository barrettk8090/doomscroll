import { useState, useEffect } from "react";

function FeedMain(){

    const [feed, setFeed] = useState([]);

    useEffect(() => {
        fetch(`/api/feeds`)
            .then(r => r.json())
            .then(data => setFeed(data))
    }, []);

    const feedName = feed.map((feed) => { return <p>{feed.name}</p> });


    return (
        <div>
            <h2>Feed Main</h2>
            <p>{feedName}</p>
        </div>
    )
}

export default FeedMain