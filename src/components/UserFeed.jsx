import { useEffect, useState } from "react"

function UserFeed({supabase}){

    const [barrettFetchError, setBarrettFetchError] = useState(null)
    const [barrettFeed, setBarrettFeed] = useState(null)

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

    return(
        <>
        <h2> Users Feed</h2>
        {barrettFetchError && <p>{barrettFetchError}</p>}
            {barrettFeed && (
                <div>
                    {console.log(barrettFeed)}
                    {barrettFeed.map(singleItem => 
                    <div>
                        <p>{singleItem.news_item_id.title}</p>
                        <p>{singleItem.news_item_id.url}</p>
                        <p>{singleItem.news_item_id.source}</p>
                    </div>)}
                </div>
            )}
            </>
    )
    
}

export default UserFeed