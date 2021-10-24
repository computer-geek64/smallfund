import Card from './Card';

const Products = () => {
    return (
        <div className="products-container" name="products">
            <div className="product-description">
                <span className="product-heading">BEST SELLERS</span>
                <span className="product-subheading">The best value for you</span>
                <span className="product-text">
                    These products have been choosen for their quality, resale value
                    and overall reuseability.
                </span>
            </div>
            <Card 
                itemId="40"
                img="https://images.pexels.com/photos/7520587/pexels-photo-7520587.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
                itemName="sample"
                price="200.00"
            />
        </div>
    )
}

export default Products;