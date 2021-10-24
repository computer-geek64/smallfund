import FileUpload from './FileUpload';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
});
const NewListing = () => {
    return (
        <ThemeProvider theme={darkTheme}>
            <div className="listing-container ">
                <span className="main-text"> Upload new product </span>
                <FileUpload />
            </div>
        </ThemeProvider>
    )
}

export default NewListing;
