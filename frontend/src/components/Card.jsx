const Card = (props) => {
    return (
        <div className="card-container">
            <a className="item-img" href={"/" + props.itemId}><img className="item-img" src={props.img} alt={props.itemName}/></a>
            <span className="item-name">{props.itemName}</span>
            <span className="item-price">${props.price}</span>
        </div>
    )
}

export default Card;