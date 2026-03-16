const express= require('express');
const axios=require('axios');
require('dotenv').config();


const app=express();

const PORT=3000;
app.set('view engine','ejs');
app.use(express.urlencoded({ extended: true }));
app.get('/',(req,res)=>{
    const ctime= new Date();
    res.render('index',{ date: ctime.toLocaleString() });
});
app.post('/submit',async (req,res)=>{
    const name=req.body.name;
    const pword=req.body.password;
    try{
        const response= await axios.post(process.env.F_URL+'/submit',{
            name:name,
            password:pword
        });
        res.send(response.data);
    }catch(error){
        res.send("Server connection failed!");
    }
});

app.get('/view',async (req,res)=>{
    try{
        const response= await axios.get(process.env.F_URL+'/view');
        res.json(response.data);
    }catch(error){
        res.send("server connection error!");
    }
});

app.post('/search',async (req,res)=>{
    const name=req.body.name;
    try{
        const response=await axios.post(process.env.F_URL+'/search',{
            name:name
        });
        res.json(response.data);
    }catch(error){
        res.send("Server connection error!");
    }
});

app.listen(PORT,()=>{
    console.log(`Server running at http://localhost:${PORT}`);
});