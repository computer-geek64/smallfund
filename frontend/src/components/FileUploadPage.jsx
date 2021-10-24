import { useState, useRef } from 'react';
import axios from 'axios';

function FileUploadPage() {
	const [selectedFile, setSelectedFile] = useState(null);
	const [productName, setProductName] = useState(null);
	const [description, setDescripton] = useState(null);
	const [price, setPrice] = useState(null);

	const [isSelected, setIsSelected] = useState(false);
	const form = useRef(null)

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = (event) => {
		event.preventDefault();
		console.log(form.current)
		const formData = new FormData(form.current);

		// formData.append('name', productName);
		// formData.append('description', description);
		// formData.append('price', price);
		// formData.append('image', selectedFile);

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
	};

	return(
   		<form ref={form} onSubmit={handleSubmission}>
			<input type="file" name="image" onChange={changeHandler} />
			{/* {isSelected ? (
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
			)} */}

			<label for="fname">Name:</label>
			<input type="text" id="fname" name="name" onChange={(event) => setProductName(event.target.value)}/>
			<label for="lname">Description:</label>
			<input type="text" id="lname" name="description" onChange={(event) => setDescripton(event.target.value)}/>
			<label for="lname">Price:</label>
			<input type="text" id="lname" name="price" onChange={(event) => setPrice(event.target.value)}/>
			<div>
				<button disabled={productName == null}> Submit</button>
			</div>
		</form>
	)
}

export default FileUploadPage;