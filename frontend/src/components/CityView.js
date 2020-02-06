import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {
    Grid,
    Typography,
    List,
    ListItem,
    Divider,
    ListItemText,
    ListItemAvatar,
    Avatar
} from '@material-ui/core';
import { useQuery } from '@apollo/react-hooks';
import { CITY_DETAIL_QUERY } from '../queries.js';

const useStyles = makeStyles(theme => ({
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
  },
  list: {
    width: '100%',
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
  inline: {
    display: 'inline',
  },
}));

export default function CityView(props) {

    const classes = useStyles();

    const slug = props.match.params.slug
    const { loading, error, data } = useQuery(CITY_DETAIL_QUERY, {
        variables: { slug }
    })

    if (loading) return 'Loading...';
    if (error) return `Error! ${error.message}`;

    const city = data.allCities.edges[0].node;

    function loadVenue() {
        console.log("coucou");
    };

    function VenueMenu() {
        return(
            <List className={classes.list}>
            {city.venues.edges.map(venue => (
                <>
                <ListItem alignItems="flex-start" onMouseOver={() => loadVenue()}>
                    <ListItemAvatar>
                        <Avatar>
                            {venue.node.venueType}
                        </Avatar>
                    </ListItemAvatar>
                    <ListItemText
                      primary={venue.node.name}
                      secondary={
                        <React.Fragment>
                          <Typography
                            component="span"
                            variant="body2"
                            className={classes.inline}
                            color="textPrimary"
                          >
                            {venue.node.venueLabel}
                          </Typography>
                          {" — I'll be in your neighborhood doing errands this…"}
                        </React.Fragment>
                      }
                    />
                  </ListItem>
                  <Divider variant="inset" component="li" />
                </>
            ))}
            </List>
        );
    }

    return(
        <div className={classes.root}>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <Typography variant="h2">{city.name}</Typography>
                </Grid>
                <Grid item xs={4}>
                    <VenueMenu/>
                </Grid>
                <Grid item xs={8}>Contenu de la fiche resto</Grid>
            </Grid>
        </div>
    );
};