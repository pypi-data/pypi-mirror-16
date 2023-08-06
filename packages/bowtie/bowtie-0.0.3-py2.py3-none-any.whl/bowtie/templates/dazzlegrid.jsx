import React from 'react';
import ReactDataGrid from 'react-data-grid';

export default class Grid extends React.Component {

    constructor(props) {
        super(props);
        this.state = {};
        this.state['data'] = [
            { id: '1', firstName: 'John', lastName: 'Bobson'},
            { id: '2', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '3', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '4', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '5', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '6', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '7', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '8', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '9', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '10', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '11', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '12', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '13', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '14', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '15', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '16', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '17', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '18', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '19', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '20', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '21', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '22', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '23', firstName: 'Bob', lastName: 'Mclaren'},
            { id: '24', firstName: 'Bob', lastName: 'Mclaren'}
        ];
        this.state['columns'] = [
            { key: 'id', name: 'ID' },
            { key: 'firstName', name: 'First'},
            { key: 'lastName', name: 'Last'}
        ];

        this.rowGetter = this.rowGetter.bind(this);
    }

    rowGetter(i) {
        return this.state.data[i];
    }

    render() {

        return (
            <ReactDataGrid
                columns={this.state.columns}
                rowGetter={this.rowGetter}
                rowsCount={this.state.data.length}
                minHeight={500}
                />
        );
    }
}

Grid.propTypes = {
    uuid: React.PropTypes.string.isRequired,
    socket: React.PropTypes.object.isRequired
};
