import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

import SearchIcon from '@mui/icons-material/Search';
import AccountCircle from '@mui/icons-material/AccountCircle';
import ControlPointIcon from '@mui/icons-material/ControlPoint';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';

export default function PrimarySearchAppBar() {
  const menuId = 'primary-search-account-menu';
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
            <Typography
                variant="h6"
                noWrap
                component="div"
                sx={{ display: { xs: 'none', sm: 'block' } }}
            >
                HackGT 8
            </Typography>
            <Box sx={{ flexGrow: 1 }} />
            <Autocomplete
                id="combo-box-demo"
                options={["abc", "bcd"]}
                getOptionLabel={(option) => option}
                forcePopupIcon={true}
                popupIcon={<SearchIcon />}
                renderInput={(params) => (
                    <>
                        <TextField
                            placeholder="search"
                            {...params}
                            label="Search..."
                            variant="filled"
                        />
                    </>
                )}
                sx={{ width: 300 }}
                size="small"
             />
            <Box sx={{ flexGrow: 1 }} />
            <IconButton
                size="large"
                edge="end"
                aria-label="add product"
                aria-controls={menuId}
                aria-haspopup="true"
                color="inherit"
            >
                <ControlPointIcon />
            </IconButton>
            <IconButton
                size="large"
                edge="end"
                aria-label="account of current user"
                aria-controls={menuId}
                aria-haspopup="true"
                color="inherit"
            >
                <AccountCircle />
            </IconButton>
            <IconButton
                size="large"
                edge="end"
                aria-label="account of current user"
                aria-controls={menuId}
                aria-haspopup="true"
                color="inherit"
            >
                <ExitToAppIcon />
            </IconButton>
        </Toolbar>
      </AppBar>
    </Box>
  );
}