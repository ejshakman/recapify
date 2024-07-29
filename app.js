// Temp data for purpose of writing script
const jsonData = [
  {
    "spotify_track_uri": "Most Skipped URI",
    "master_metadata_track_name": "Most Skipped Track",
    "master_metadata_album_artist_name": "Most Skipped Artist",
    "master_metadata_album_album_name": "Most Skipped Album",
    "skipped": "true"
  },
  {
    "spotify_track_uri": "Most Skipped URI",
    "master_metadata_track_name": "Most Skipped Track",
    "master_metadata_album_artist_name": "Most Skipped Artist",
    "master_metadata_album_album_name": "Most Skipped Album",
    "skipped": "true"
  },
  {
    "spotify_track_uri": "Most Skipped URI",
    "master_metadata_track_name": "Not Most Skipped Track",
    "master_metadata_album_artist_name": "Not Most Skipped Artist",
    "master_metadata_album_album_name": "Not Most Skipped Album",
    "skipped": "true"
  },
  {
    "spotify_track_uri": "Not Skipped URI",
    "master_metadata_track_name": "Not Skipped Track",
    "master_metadata_album_artist_name": "Not Skipped Artist",
    "master_metadata_album_album_name": "Not Skipped Album",
    "skipped": "false"
  }
];


// Function to initialize the Map
function initializeMap() {
  return new Map();
}


// Recursive function to process data and count key-value pairs
function processItems(map, data, key, value, index = 0) {
  if (index >= data.length) {
    return map;
  }

  const item = data[index];

  // Add item to map if entry does not exist
  if (!map.has(item.spotify_track_uri)) {
    map.set(item.spotify_track_uri, {
      count: 0,
      track: item.master_metadata_track_name,
      artist: item.master_metadata_album_artist_name,
      album: item.master_metadata_album_album_name
    });
  }

  // Update count if key-value pair matches
  if (item[key] === value) {
    map.set(item.spotify_track_uri, {
      count: map.get(item.spotify_track_uri).count + 1,
      track: map.get(item.spotify_track_uri).track,
      artist: map.get(item.spotify_track_uri).artist,
      album: map.get(item.spotify_track_uri).album
    });
  }

  // Call processItems function
  return processItems(map, data, key, value, index + 1);
}


// Function to find the uri with the most occurrences of key-value matches
function findUriWithMostMatches(map) {
  let maxCount = 0;
  let maxUri = null;
  let track = '';
  let artist = '';
  let album = '';

  // Update maxCount and item information if them item has more occurrences than the previous highest count
  map.forEach((value, spotify_track_uri) => {
    if (value.count > maxCount) {
      maxCount = value.count;
      maxUri = spotify_track_uri;
      track = value.track;
      artist = value.artist;
      album = value.album;
    }
  });

  // Return information for item with the most occurrences of key-value matches
  return {
    spotify_track_uri: maxUri,
    track: track,
    artist: artist,
    album: album,
    count: maxCount
  };
}


// Initiate function calls and pass parameters
const map = initializeMap();
const result = processItems(map, jsonData, 'skipped', 'true');
const maxOccurrence = findUriWithMostMatches(result);


// Print the results
console.log(`${maxOccurrence.track} from ${maxOccurrence.artist}'s album ${maxOccurrence.album} is your most skipped song.`);