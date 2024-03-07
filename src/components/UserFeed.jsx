// Generates feed items for a users feed of subscribed categories

function UserFeed({singleItem}){

    return(
        <>
            <p><a target="_blank" href={singleItem.url}>{singleItem.title}</a></p>
            <p>{singleItem.source}</p>
            <p>{singleItem.url}</p>
        </>
    )
    
}

export default UserFeed