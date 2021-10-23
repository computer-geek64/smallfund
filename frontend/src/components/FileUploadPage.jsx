import { useState } from 'react';
import axios from 'axios';

function FileUploadPage() {
	const [selectedFile, setSelectedFile] = useState(null);
	const [productName, setProductName] = useState(null);
	const [description, setDescripton] = useState(null);
	const [price, setPrice] = useState(null);

	const [isSelected, setIsSelected] = useState(false);

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = () => {
		const formData = new FormData();

		console.log(productName, description)

		formData.append('name', productName);
		formData.append('description', description);
		formData.append('price', price);
		formData.append('image', selectedFile);

		const config = {
			method: "post",
			url: "http://128.61.105.83:8000/",
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
	};

	return(
   		<div>
			<input type="file" name="file" onChange={changeHandler} />
			{isSelected ? (
				<div>
					<p>Filename: {selectedFile.name}</p>
					<p>Filetype: {selectedFile.type}</p>
					<p>Size in bytes: {selectedFile.size}</p>
					<p>
						lastModifiedDate:{' '}
						{selectedFile.lastModifiedDate.toLocaleDateString()}
					</p>
				</div>
			) : (
				<p>Select a file to show details</p>
			)}

			<label for="fname">Name:</label>
			<input type="text" id="fname" name="fname" onChange={(event) => setProductName(event.target.value)}/>
			<label for="lname">Description:</label>
			<input type="text" id="lname" name="lname" onChange={(event) => setDescripton(event.target.value)}/>
			<label for="lname">Price:</label>
			<input type="text" id="lname" name="lname" onChange={(event) => setPrice(event.target.value)}/>
			<div>
				<button disabled={productName == null} onClick={handleSubmission}>Submit</button>
			</div>
		</div>
	)
}

export default FileUploadPage;