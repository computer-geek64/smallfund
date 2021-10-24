import { useRef, useState } from 'react';
import axios from 'axios';
import { styled } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import PhotoCamera from '@mui/icons-material/PhotoCamera';
import CompareArrowsIcon from '@mui/icons-material/CompareArrows';
import Button from '@mui/material/Button';

const Input = styled('input')({
	display: 'none',
});

  
function FileUpload() {
	const form = useRef(null)
	const [uploadedImage, setUploadedImage] = useState(null);
	const handleChange = event => {
		if (event.target.files[0]) {
			let url = URL.createObjectURL(event.target.files[0])
			setUploadedImage(url)
		} else {
			setUploadedImage(null)
		}
	}

	const handleSubmission = event => {
		event.preventDefault();
		const formData = new FormData(form.current);
		var object = {};
		formData.forEach(function(value, key){
			object[key] = value;
		});

		const config = {
			method: "post",
			url: "http://128.61.105.83:8000/upload",
			data: formData,
			headers: { "Content-Type": "multipart/form-data" },
		}

		axios(config)
		.then(function (response) {
			console.log(JSON.stringify(response.data));
		})
		.catch(function (error) {
			console.log(error);
		});

		form.current.reset();
		setUploadedImage(null);
	};

	return(
   		<form ref={form} onSubmit={handleSubmission}>
			
			<div className="form-inputs">
				<div className="upload-image-container">
					<div>
						{uploadedImage && <img className="uploaded-image" src={uploadedImage} alt="uploadedImage"/>}
						<label htmlFor="icon-button-file">
							<Input accept="image/*" id="icon-button-file" type="file" name="image" onChange={handleChange}/>
							<IconButton color="primary" component="span" size="large">
								{uploadedImage ? <CompareArrowsIcon /> : <PhotoCamera/>}
							</IconButton>
							{!uploadedImage ? <div>Upload Image</div> : <div>Replace Image</div>}
						</label>
					</div>
				</div>

				<div className="file-upload-text-fields">
					<TextField label="Product name" name="name" variant="outlined" required />
					<div className="spacer"></div>
					<TextField label="Description" name="description" variant="outlined" required multiline rows={4}/>
					<div className="spacer"></div>
					<TextField label="Price" name="price" variant="outlined" required/>
					<div className="spacer"></div>

					<div>
					<Button type="submit" variant="contained"> Submit</Button>
					</div>
				</div>
			</div>

		</form>
	)
}

export default FileUpload;