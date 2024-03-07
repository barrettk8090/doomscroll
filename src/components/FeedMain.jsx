import { useState, useEffect } from "react";
import UserFeed from "./UserFeed";

function FeedMain({supabase}){

    // const [feed, setFeed] = useState([]);

    // useEffect(() => {
    //     fetch(`/api/feeds`)
    //         .then(r => r.json())
    //         .then(data => setFeed(data))
    // }, []);

    // const feedName = feed.map((feed) => { return <p>{feed.name}</p> });

    const [fetchError, setFetchError] = useState(null)
    const [category, setCategory] = useState(null)

    const [barrettFetchError, setBarrettFetchError] = useState(null)
    const [barrettFeed, setBarrettFeed] = useState(null)

    useEffect(() => {
        const fetchCategories = async () => {
            const {data, error} = await supabase
                .from("category")
                .select()

            if (error) {
                setFetchError("Error fetching categories")
                setCategory(null)
                console.log(error)
            }
            if (data) {
                setCategory(data)
                setFetchError(null)
            }    
        }
        fetchCategories()
    }, [])

    useEffect(() => {
        const fetchBarrettFeed = async () => {
            const {data, error} = await supabase
                .from("user_feed_news")
                .select("*,news_item_id(*),user_feed_id(*)")

            if (error) {
                setBarrettFetchError("Error fetching categories")
                setBarrettFeed(null)
                console.log(error)
            }
            if (data) {
                setBarrettFeed(data)
                setBarrettFetchError(null)
            }    
        }
        fetchBarrettFeed()
    }, [])

    return (
        <div>
            <h2>Feed Main</h2>
            <h2> Users Feed</h2>
        {barrettFetchError && <p>{barrettFetchError}</p>}
            {barrettFeed && (
                <div>
                    {console.log(barrettFeed)}
                    {barrettFeed.map(singleItem => 
                        <UserFeed singleItem={singleItem} key={singleItem.id}/>)}
                </div>
            )}
            {fetchError && <p>{fetchError}</p>}
            {category && (
                <div>
                    {category.map(singleCat => (
                        <p>{singleCat.name}</p>
                    ))}
                </div>
                
                
            )}
        </div>
    )
}

export default FeedMain