import { useState, useEffect } from "react";
import UserFeed from "./UserFeed";
import CategoryFeed from "./CategoryFeed";

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

    const [userFetchError, setUserFetchError] = useState(null)
    const [userFeed, setUserFeed] = useState(null)

    const [categoryFetchError, setCategoryFetchError] = useState(null)
    const [categoryFeed, setCategoryFeed] = useState(null)

    {/* Get all categories from Supabase */}
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

    {/* Get a categories feed from Supabase */}
    useEffect(() => {
        const fetchCategoryFeed = async () => {
            const {data, error} = await supabase
                .from("news_item")
                // Selecting ONLY category ID 1 - bird flu. Need to make this dynamic
                .select("*")
                .eq("category_id", 1)

            if (error) {
                setCategoryFetchError("Error fetching category feed")
                setCategoryFeed(null)
                console.log(error)
            }
            if (data) {
                setCategoryFeed(data)
                setCategoryFetchError(null)
            }    
        }
        fetchCategoryFeed()
    }, [])

    {/* Get a users feed from supabase */}
    useEffect(() => {
        const fetchUserFeed = async () => {
            const {data, error} = await supabase
                .from("user_feed_news")
                .select("*,news_item_id(*),user_feed_id(*)")

            if (error) {
                setUserFetchError("Error fetching categories")
                setUserFeed(null)
                console.log(error)
            }
            if (data) {
                setUserFeed(data)
                setUserFetchError(null)
            }    
        }
        fetchUserFeed()
    }, [])

    return (
        <div>
            <h1 className="font-display">Your Feeds</h1>

            {/* USER FEED – JUST BARRETT FOR NOW */}

            <div className="border-2">
                <h2>Users Feed</h2>
                    {userFetchError && <p>{userFetchError}</p>}
                        {userFeed && (
                            <div>
                                {/* {console.log(userFeed)} */}
                                {userFeed.map(singleItem => 
                                    <UserFeed singleItem={singleItem.news_item_id} key={singleItem.id}/>)}
                            </div>
                        )}
            </div>

            {/* CATEGORY FEED – JUST BIRD FLU FOR NOW */}

            <div className="border-2">
                <h2>Category Feed</h2>
                    {categoryFetchError && <p>{categoryFetchError}</p>}
                        {categoryFeed && (
                            <div>
                                {console.log(categoryFeed)}
                                {categoryFeed.map(singleCat => 
                                    <CategoryFeed singleCat={singleCat} key={singleCat.id}/>)}
                            </div>
                        )}
            </div>

            {/* CATEGORIES LISTED */}

            <div className="border-2">                        
                {fetchError && <p>{fetchError}</p>}
                {category && (
                    <div>
                        {category.map(singleCat => (
                            <p>{singleCat.name}</p>
                        ))}
                </div>
                
                
            )}
            </div>

        </div>
    )
}

export default FeedMain