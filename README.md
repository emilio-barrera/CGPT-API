<h1>CGPT-API</h1>
<p>Personal project to learn how to use chat gpt's API</p>

<h2>Getting Started</h2>
<p>
    <strong>Create image:</strong><br>
    Clone the repository and then open a terminal pointing to it. Then, run the following command:
</p>
<code>docker build -t 'gpt' .</code>
<p>
    <strong>Run the image:</strong><br>
    After the image has been built, you should now be able to run it by executing the following command. You will want to mount the repository folder into it so you can work directly into the terminal
</p>
<code>docker run --name "gpt" --volume "/path/to/repo/CGPT-API/:/mnt/CGPT-API/" -dt gpt</code>
<p>
    <strong>Access the container's BASH:</strong><br>
    Once the image is running you will now be able to access its bash with:
</p>
<code>docker exec -ti gpt bash</code>
<p>
    Once you are in, you can access the repo by changing into the directory
</p>
<code>cd /mnt/CGPT-API/</code>