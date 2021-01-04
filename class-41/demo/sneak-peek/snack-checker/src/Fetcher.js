import axios from 'axios'

async function fetchResource(options) {

    const url = options.base + "/api/token/";

    const response = await axios.post(url, {
      username: options.username,
      password: options.password
    });

    const { access } = response.data;

    const config = {
      headers: { Authorization: `Bearer ${access}` }
    };

    const snacksResponse = await axios.get(`${options.base}/api/v1/${options.resource}/`, config);

    return snacksResponse.data;

}

export default fetchResource
