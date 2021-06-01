const express = require("express");

const app = express();

app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

app.listen(process.env.PORT || 8900);
