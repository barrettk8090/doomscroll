// Generates feed items for a users feed of subscribed categories

function UserFeed({singleItem}){

    return(
        <>
            <p><a target="_blank" href={singleItem.news_item_id.url}>{singleItem.news_item_id.title}</a></p>
            <p>{singleItem.news_item_id.source}</p>
            <p>{singleItem.news_item_id.url}</p>
        </>
    )
    
}

export default UserFeed