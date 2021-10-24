import Typewriter from 'typewriter-effect';
import FancyButton from './FancyButton';

const Home = () => {
    return (
        <div className="home-container ">
            <span className="home-main-text">
                Find your next 
                <div className="home-header-padding"></div>
                <Typewriter
                    options={{
                        strings: ['home upgrade', 'table', 'passion'],
                        autoStart: true,
                        loop: true
                    }}
                />
            </span>
            <div className="spacer"></div>
            <FancyButton/>
        </div>
)
}

export default Home;