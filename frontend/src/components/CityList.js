import React from 'react';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import { useQuery } from '@apollo/react-hooks';
import { ALL_CITIES } from '../queries.js';


const useStyles = makeStyles({
  card: {
    maxWidth: 345,
  },
  media: {
    height: 140,
  },
});

export default function CityList(props) {
    const classes = useStyles();
    const { loading, error, data, refetch } = useQuery(ALL_CITIES);

    if (loading) return 'Loading...';
    if (error) return `Error! ${error.message}`;

    console.log(data)
    return(
        <div>
            <Typography variant="h2">All cities</Typography>
            <Button color="primary" onClick={() => refetch()}>Refetch</Button>
            {data.allCities.edges.map(city => (

                <Card className={classes.card} key={city.node.id}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image="/static/images/cards/contemplative-reptile.jpg"
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {city.node.name}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging
            across all continents except Antarctica
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Share
        </Button>
        <Button size="small" color="primary">
          Learn More
        </Button>
      </CardActions>
    </Card>

            ))}
        </div>
    );
};