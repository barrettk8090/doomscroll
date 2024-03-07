
function CategoryFeed({singleCat}){
    return(
        <>
            <p><a href={singleCat.url}>{singleCat.title}</a></p>
            <p>{singleCat.source}</p>
            <p>{singleCat.created_at}</p>
        </>
    )
}

export default CategoryFeed