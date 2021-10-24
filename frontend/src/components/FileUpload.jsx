import { useRef, useState } from 'react';
import axios from 'axios';
import { styled } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import PhotoCamera from '@mui/icons-material/PhotoCamera';
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
		console.log(object)

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
	};

	return(
   		<form ref={form} onSubmit={handleSubmission}>
			
			<div className="form-inputs">
				<div className="upload-image-container">
				{!uploadedImage && 
					<label htmlFor="icon-button-file">
						<Input accept="image/*" id="icon-button-file" type="file" name="image" onChange={handleChange}/>
						<IconButton color="primary" component="span" large>
							<PhotoCamera />
						</IconButton>
					</label>
				}
				</div>

				{uploadedImage && <img className="uploaded-image" src={uploadedImage} alt="uploadedImage"/>}

				<div className="file-upload-text-fields">
					<TextField label="Product name" name="name" variant="outlined" required />
					<TextField label="Description" name="description" variant="outlined" required multiline rows={4}/>
					<TextField label="Price" name="price" variant="outlined" required/>
				</div>
			</div>

			<Button type="submit" variant="contained"> Submit</Button>
		</form>
	)
}

export default FileUpload;