import { useState, useEffect } from "react";

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

    return (
        <div>
            <h2>Feed Main</h2>
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