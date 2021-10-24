import AcUnitIcon from '@mui/icons-material/AcUnit';
import DeleteIcon from '@mui/icons-material/Delete';
import StorefrontIcon from '@mui/icons-material/Storefront';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';

const AdvantageCards = () => {
    return (
        <div className="filler">
            <div className="advantage-card">
                <AcUnitIcon fontSize="large"/>
                <span className="advantage-text">Environment</span>
                <span className="advantage-disc"> 
                    Buying returned items prevent them from being incarcerated.
                </span>
            </div>

            <div className="advantage-card">
                <DeleteIcon fontSize="large"/>
                <span className="advantage-text">Waste Reduction</span>
                <span className="advantage-disc"> 
                    Reduce waste and prevent returned products from ending up in landfills.
                </span>
            </div>

            <div className="advantage-card">
                <StorefrontIcon fontSize="large"/>
                <span className="advantage-text">Go Local</span>
                <span className="advantage-disc"> 
                    Support local businesses by helping them recoup a part of their loss.
                </span>
            </div>

            <div className="advantage-card">
                <AttachMoneyIcon fontSize="large"/>
                <span className="advantage-text">Spend less, Save Big</span>
                <span className="advantage-disc"> 
                    Spend less and save more by using near mint quality items.
                </span>
            </div>
        </div>
    )
}

export default AdvantageCards;