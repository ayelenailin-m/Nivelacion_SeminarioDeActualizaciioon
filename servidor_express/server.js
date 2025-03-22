const express = require("express");
const path = require("path");
const app = express();

// servir los archivos estáticos 
app.use(express.static(__dirname));
// ruta para envías el html
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../index.html"));
});

// iniciar el servidor
app.listen(3000, () => {
    console.log("Servidor iniciado en http://localhost:3000");
});