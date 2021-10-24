import { useRef } from 'react';
import axios from 'axios';

function FileUploadPage() {
	const form = useRef(null)

	const handleSubmission = event => {
		event.preventDefault();
		const formData = new FormData(form.current);
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
			<input type="file" name="image" />

			<label for="fname">Name:</label>
			<input type="text" id="fname" name="name" />

			<label for="lname">Description:</label>
			<input type="text" id="lname" name="description" />

			<label for="lname">Price:</label>
			<input type="text" id="lname" name="price"/>
			<div>
				<button> Submit</button>
			</div>
		</form>
	)
}

export default FileUploadPage;