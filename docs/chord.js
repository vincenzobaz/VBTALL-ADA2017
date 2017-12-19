
function chord(divId, data, h) {
    data = _.sortBy(data, f => -f.dead_sides).slice(0, 30);

    const sides = new Set([...data.map(f => f.name_a), ...data.map(f => f.name_b)]);
    let nodes = Array.from(sides);

    let mat = [];
    for (let i = 0; i < nodes.length; i++) {
        mat.push([]);
        for (let j = 0; j < nodes.length; j++) {
            mat[i].push(0);
        }
    }

    const linkColor = d3.scaleLinear()
        .domain([_.min(data.map(el => el.dead)), _.max(data.map(el => el.dead))])
        .range(['steelblue', 'red']);

    nodes = nodes.map((s, i) => ({
        node: i,
        name: s,
    }));

    const nameToId = {};
    nodes.forEach(s => nameToId[s.name] = s.node);
    const idToName = {};
    nodes.forEach(s => idToName[s.node] = s.name);

    for (let fight of data) {
        mat[nameToId[fight.name_a]][nameToId[fight.name_b]] = fight.dead_b;
        mat[nameToId[fight.name_b]][nameToId[fight.name_a]] = fight.dead_a;
    }

    let width = d3.select(`#${divId}`).node().clientWidth; //900;
    let height = d3.select(`#${divId}`).node().clientHeight - h; //1000;

    const margin = { top: 10, right: 10, bottom: 10, left: 10 };
    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;

    const svg = d3.select(`#${divId}`).append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.right})`);

    const outerRadius = Math.min(width, height) * 0.5;// - 40;
    const innerRadius = outerRadius - 40;

    const chord = d3.chord().padAngle(0.02).sortSubgroups(d3.descending);

    const arc = d3.arc().innerRadius(innerRadius).outerRadius(outerRadius);

    const ribbon = d3.ribbon().radius(innerRadius);

    const fade = opacity => (gc, i) => {
        g.selectAll(".ribbons path")
            .filter(d => d.source.index != gc.index && d.target.index != gc.index)
            .transition()
            .style("opacity", opacity);
    };

    const g = svg.append('g')
        .attr('transform', `translate(${+width / 2}, ${height / 2})`)
        .datum(chord(mat));

    const group = g.append('g')
        .attr('class', 'groups')
        .selectAll('g')
        .data(chords => chords.groups)
        .enter().append('g')
        .on('mouseover', fade(0.1)).on('mouseout', fade(0.7));

    group.append('path')
        .style('fill', d => linkColor(d.value))
        .attr('id', (d, i) => 'arc' + i)
        .attr('d', arc);

    group.append('title').text(d => idToName[d.index] + '\nvictims ' + d.value);

    /*
    group.append('text')
        .attr('x', 5)
        .attr('dy', 18)
        .append('textPath')
        .attr('text-anchor', 'start')
        .style('font-family', 'arial')
        .attr('xlink:href', (d, i) => '#arc' + i)
        .text(d => idToName[d.index]);
    */

    const link = g.append('g')
        .attr('class', 'ribbons')
        .selectAll('path')
        .data(chords => chords)
        .enter().append('path')
        .attr('d', ribbon)
        .style('fill', d => linkColor(d.source.value))
        .style('opacity', 0.7);

    //.style('stroke', 'blue')
    link.append('title').text(d => idToName[d.source.index] + ' -> ' + idToName[d.target.index] + '\n' + d.source.value);

}

function chordByRegion(divName, data) {
    const regionsToData = _.groupBy(data, 'region');
    const regions = _.keys(regionsToData);
    const ul = d3.select(`#${divName}`)
        .append('ul')
        .attr('class', `nav nav-tabs nav-justified`);

    ul.selectAll('li')
        .data(regions)
        .enter()
        .append('li')
        .attr('role', 'presentation')
        .attr('class', (d, i) => i == 0 ? 'active' : null)
        .attr('id', d => d.replace(' ', '-'))
        .html(d => `<a>${d}</a>`)
        .on('click', d => {
            ul.selectAll('li').attr('class', db => db == d ? 'active' : null);

            d3.select('#' + divName).select('svg').remove();
            chord(divName, regionsToData[d], ul.node().clientHeight);
        })
    chord(divName, regionsToData[regions[0]], ul.node().clientHeight);
}
