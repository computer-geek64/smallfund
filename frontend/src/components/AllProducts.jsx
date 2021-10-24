import { useState } from 'react';
import Card from './Card';

const AllProducts = () => {
    const [items, setItems] = useState([0,0,0,0,0,0,0,0])
    return (
        <div className="all-products-container" name="all-products">
            <span className="all-products-heading">ALL PRODUCTS</span>
            <div className="all-products-container-layer" name="products">
                {items.map(() => 
                    <Card 
                        itemId="40"
                        img="https://images.pexels.com/photos/7520587/pexels-photo-7520587.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
                        itemName="sample"
                        price="200.00"
                    />
                )}
            </div>
        </div>
    )
}

export default AllProducts;