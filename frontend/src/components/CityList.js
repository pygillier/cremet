import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {
  Typography,
  Grid,
  Button,
  Card,
  CardActionArea,
  CardActions,
  CardContent,
  CardMedia,
  IconButton,
} from '@material-ui/core';
import { Favorite, Add } from '@material-ui/icons';
import { useQuery } from '@apollo/react-hooks';
import { Link as RouterLink } from 'react-router-dom';
import { CITY_LIST_QUERY } from '../queries.js';


const useStyles = makeStyles({
  root: {
    flexGrow: 1,
  },
  card: {
    maxWidth: 345,
  },
  media: {
    height: 140,
  },
  buttons: {
    justifyContent: 'space-between',
  }
});



export default function CityList(props) {
    const classes = useStyles();
    const { loading, error, data, refetch } = useQuery(CITY_LIST_QUERY);

    if (loading) return 'Loading...';
    if (error) return `Error! ${error.message}`;

    function setCurrentCity(city) {
      props.setCurrentCity({name: city.node.name, slug: city.node.slug, id: city.node.id})
    }

    function isCurrentCity(slug) {
      return props.currentCity.slug !== slug;
    }

    return(
      <div className={classes.root}>
        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Typography variant="h2">All cities</Typography>
            <Button color="primary" onClick={() => refetch()}>Refetch</Button>
          </Grid>
          {data.allCities.edges.map(city => (
            <Grid item xs={12} sm={4} key={city.node.id}>
              <Card className={classes.card}>
                <CardActionArea component={RouterLink} to={`/cities/${city.node.slug}`}>
                  <CardMedia className={classes.media}
                    image="/static/images/cards/contemplative-reptile.jpg"
                    title="Contemplative Reptile"
                    />
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                      {city.node.name}
                    </Typography>
                    <Typography variant="body2" color="textSecondary" component="p">
                      There are {city.node.venuesCount} venues in this city.
                    </Typography>
                  </CardContent>
                </CardActionArea>
                <CardActions className={classes.buttons}>
                {isCurrentCity(city.node.slug) &&
                  <IconButton
                    size="small"
                    color="secondary"
                    onClick={() => setCurrentCity(city)}>
                    <Favorite/>
                  </IconButton>
                }
                  <IconButton
                    size="small"
                    color="action"
                  >
                    <Add/>
                  </IconButton>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      </div>
    );
};