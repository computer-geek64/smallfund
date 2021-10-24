import ControlPointIcon from '@mui/icons-material/ControlPoint';

const Card = (props) => {
    return (
        <div className="card-container">
            <div className="spl-container">
                <img className="item-img" src={props.img} alt={props.itemName}/>
                <a href={"/product/" + props.itemId}>
                    <div class="overlay">
                        <ControlPointIcon className="icon"/>
                    </div>
                </a>
            </div>
            <span className="item-name">{props.itemName}</span>
            <span className="item-price">${props.price}</span>
        </div>
    )
}

export default Card;