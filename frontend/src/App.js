import Main from './components/Main'
import NewListing  from './components/NewListing';
import FileUploadPage from './components/FileUploadPage';
import './App.css';

function App() {
  // const getText = () => {
  //   const config = {
  //     method: 'get',
  //     url: 'http://128.61.105.83:8000/',
  //     headers: { }
  //   };
    
  //   axios(config)
  //   .then(function (response) {
  //     setData(JSON.stringify(response.data));
  //   })
  //   .catch(function (error) {
  //     console.log(error);
  //   });
  // }

  return (
    <div className="App">
      <Main/>
      <NewListing/>
      <FileUploadPage/>
    </div>
  );
}

export default App;
