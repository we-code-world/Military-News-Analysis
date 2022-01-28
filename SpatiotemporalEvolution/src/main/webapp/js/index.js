let canvas, ctx;
let render, init;
let surface;


class Noise {
    constructor(r) {
        if (r == undefined) r = Math;
        this.grad3 = [[1, 1, 0], [-1, 1, 0], [1, -1, 0], [-1, -1, 0],
            [1, 0, 1], [-1, 0, 1], [1, 0, -1], [-1, 0, -1],
            [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1]];
        this.p = [];
        for (var i = 0; i < 256; i++) {
            this.p[i] = Math.floor(r.random() * 256);
        }
        // To remove the need for index wrapping, double the permutation table length
        this.perm = [];
        for (var i = 0; i < 512; i++) {
            this.perm[i] = this.p[i & 255];
        }
    }

    dot(g, x, y, z) {
        return g[0] * x + g[1] * y + g[2] * z;
    }

    mix(a, b, t) {
        return (1.0 - t) * a + t * b;
    }

    fade(t) {
        return t * t * t * (t * (t * 6.0 - 15.0) + 10.0);
    }

    noise(x, y, z) {
        // Find unit grid cell containing point
        var X = Math.floor(x);
        var Y = Math.floor(y);
        var Z = Math.floor(z);

        // Get relative xyz coordinates of point within that cell
        x = x - X;
        y = y - Y;
        z = z - Z;

        // Wrap the integer cells at 255 (smaller integer period can be introduced here)
        X = X & 255;
        Y = Y & 255;
        Z = Z & 255;

        // Calculate a set of eight hashed gradient indices
        var gi000 = this.perm[X + this.perm[Y + this.perm[Z]]] % 12;
        var gi001 = this.perm[X + this.perm[Y + this.perm[Z + 1]]] % 12;
        var gi010 = this.perm[X + this.perm[Y + 1 + this.perm[Z]]] % 12;
        var gi011 = this.perm[X + this.perm[Y + 1 + this.perm[Z + 1]]] % 12;
        var gi100 = this.perm[X + 1 + this.perm[Y + this.perm[Z]]] % 12;
        var gi101 = this.perm[X + 1 + this.perm[Y + this.perm[Z + 1]]] % 12;
        var gi110 = this.perm[X + 1 + this.perm[Y + 1 + this.perm[Z]]] % 12;
        var gi111 = this.perm[X + 1 + this.perm[Y + 1 + this.perm[Z + 1]]] % 12;

        // The gradients of each corner are now:
        // g000 = grad3[gi000];
        // g001 = grad3[gi001];
        // g010 = grad3[gi010];
        // g011 = grad3[gi011];
        // g100 = grad3[gi100];
        // g101 = grad3[gi101];
        // g110 = grad3[gi110];
        // g111 = grad3[gi111];
        // Calculate noise contributions from each of the eight corners
        var n000 = this.dot(this.grad3[gi000], x, y, z);
        var n100 = this.dot(this.grad3[gi100], x - 1, y, z);
        var n010 = this.dot(this.grad3[gi010], x, y - 1, z);
        var n110 = this.dot(this.grad3[gi110], x - 1, y - 1, z);
        var n001 = this.dot(this.grad3[gi001], x, y, z - 1);
        var n101 = this.dot(this.grad3[gi101], x - 1, y, z - 1);
        var n011 = this.dot(this.grad3[gi011], x, y - 1, z - 1);
        var n111 = this.dot(this.grad3[gi111], x - 1, y - 1, z - 1);
        // Compute the fade curve value for each of x, y, z
        var u = this.fade(x);
        var v = this.fade(y);
        var w = this.fade(z);
        // Interpolate along x the contributions from each of the corners
        var nx00 = this.mix(n000, n100, u);
        var nx01 = this.mix(n001, n101, u);
        var nx10 = this.mix(n010, n110, u);
        var nx11 = this.mix(n011, n111, u);
        // Interpolate the four results along y
        var nxy0 = this.mix(nx00, nx10, v);
        var nxy1 = this.mix(nx01, nx11, v);
        // Interpolate the two last results along z
        var nxyz = this.mix(nxy0, nxy1, w);

        return nxyz;
    }}



class Surface {
    constructor(points = 5, dimensions) {
        this.stage = document.createElement('canvas');
        this.stage.id = "surfaceCanvas";
        this.t = 0;
        this.noise = new Noise();

        this.dimensions = dimensions;

        this.initialise();

        this.onMouseMove = this.onMouseMove.bind(this);

        window.addEventListener('pointermove', this.onMouseMove);

        this.numPoints = points;

        this.running = true;

    }

    initialise() {
        this.points = [];
        for (let i = 0; i <= this.numPoints; i++) {
            this.points.push(new SurfacePoint(i, undefined, Math.random() * .5));
        }

        // window.p = this.points[50];
    }

    draw(ops, ctx) {
        ops.forEach(op => {
            ctx[op.name](...op.params);
    });
    }

    render(delta) {
        let ctx = this.stage.getContext('2d');

        let y = 0;
        ctx.clearRect(0, 0, this.width, this.height);

        let ops = [];
        ops.push({
            name: 'beginPath',
            params: [] });

        ops.push({
            name: 'moveTo',
            params: [0, 0] });

        ops.push({
            name: 'lineTo',
            params: [0, this.height * .5] });

        y = this.height * .5;

        this.t += .015;

        // let right = this.points[1];
        this.points.forEach((point, index) => {

            let left1 = this.points[index - 1];
        let right1 = this.points[index + 1];
        let left2 = this.points[index - 2];
        let right2 = this.points[index + 2];

        let left1Height = left1 ? left1.height : 0;
        let right1Height = right1 ? right1.height : 0;
        let left2Height = left2 ? left2.height : 0;
        let right2Height = right2 ? right2.height : 0;

        // acceleration
        point.acceleration = (-0.3 * point.height + (left1Height - point.height) + (right1Height - point.height)) * this.elasticity - point.speed * this.friction;
        point.acceleration += (-0.3 * point.height + (left2Height - point.height) + (right2Height - point.height)) * (this.elasticity / 2) - point.speed * this.friction;

        // speed
        point.speed += point.acceleration * 5;

        // height
        point.height += point.speed * 10;

        let p1 = new Vector(this.segWidth * (index - 1), y + left1Height);
        let p2 = new Vector(this.segWidth * index, y + point.height);
        var xc = (p1.x + p2.x) / 2;
        var yc = (p1.y + p2.y) / 2;
        ops.push({
            name: 'quadraticCurveTo',
            params: [p1.x, p1.y, xc, yc] });


        let sp = this.noise.noise(p1.x * .01, p1.y * .01, this.t);
        sp *= sp;
        point.speed += sp * .05;
    });

        let p1 = new Vector(this.segWidth * this.numPoints, y + this.points[this.points.length - 1].height);
        let p2 = new Vector(this.segWidth * (this.numPoints + 1), y);
        var xc = (p1.x + p2.x) / 2;
        var yc = (p1.y + p2.y) / 2;
        ops.push({
            name: 'quadraticCurveTo',
            params: [p1.x, p1.y, xc, yc] });


        ops.push({
            name: 'lineTo',
            params: [this.width, 0] });

        ops.push({
            name: 'lineTo',
            params: [0, 0] });

        ops.push({
            name: 'closePath',
            params: [] });


        ctx.globalCompositeOperation = 'source-over';

        ctx.fillStyle = this.colour;
        ctx.fillStyle = this.gradient;
        ctx.strokeStyle = 'rgba(255,255,255,1)';
        this.draw(ops, ctx);
        ctx.fill();
        // ctx.stroke();

        ctx.globalCompositeOperation = 'multiply';

        ctx.shadowOffsetX = 0;
        ctx.shadowOffsetY = -10;
        ctx.shadowBlur = 20;
        ctx.shadowColor = 'rgba(0,80,0,1)';
        this.draw(ops, ctx);
        ctx.stroke();
        ctx.stroke();
        ctx.stroke();

        if (this.running) {
            window.requestAnimationFrame(this.render.bind(this));
        }
    }

    onMouseMove(e) {

        e.preventDefault();

        let mousePos = new Vector(e.clientX, e.clientY); // The 250 here is just to make up for the offset on screen

        let difference = this.oldMousePos.subtractNew(mousePos);
        let offset = this.stage.getBoundingClientRect();

        let normalisedPos1 = mousePos.y - (offset.top + this.height / 2);
        let normalisedPos2 = this.oldMousePos.y - (offset.top + this.height / 2);

        let changed = normalisedPos1 * normalisedPos2 < 0;

        if (changed) {
            let closestPointIndex = Math.round(mousePos.x / (this.width / this.numPoints));
            let closestPoint = this.points[closestPointIndex];
            let power = Math.min(Math.max(difference.y * .2, -1), 1);
            closestPoint.speed += -power;
        }

        this.oldMousePos = mousePos;
    }

    set oldMousePos(value) {
        if (value instanceof Vector) {
            this._oldMousePos = value;
        }
    }
    get oldMousePos() {
        return this._oldMousePos instanceof Vector ? this._oldMousePos : new Vector(0, 0);
    }

    set elasticity(value) {
        if (typeof value === 'number') {
            this._elasticity = value;
        }
    }
    get elasticity() {
        return this._elasticity || 0.00007;
    }
    set friction(value) {
        if (typeof value === 'number') {
            this._friction = value;
        }
    }
    get friction() {
        return this._friction || 0.0045;
    }

    set numPoints(value) {
        let oldNumPoints = this._numPoints;
        if (typeof value == 'number' && oldNumPoints != value) {
            this._numPoints = value;
            this.initialise();
        }
    }
    get numPoints() {
        return this._numPoints;
    }

    set running(value) {
        let oldValue = this._running;
        this._running = value === true;
        if (value === true && oldValue !== true) {
            this.render();
        }
    }
    get running() {
        return this._running === true;
    }

    set stage(element) {
        if (element instanceof HTMLElement) {
            this._stage = element;
        }
    }
    get stage() {
        return this._stage;
    }

    get segWidth() {
        return this.width / this.numPoints;
    }

    set dimensions(value) {
        if (value instanceof Vector) {
            this._dimensions = value;
            this.width = value.width;
            this.height = value.height;
        }
    }
    get dimensions() {
        return this._dimensions || null;
    }

    set width(value) {
        if (typeof value == 'number') {
            this._width = value;
            this.stage.width = this._width;
        }
    }
    get width() {
        return this._width || window.innerWidth;
    }
    set height(value) {
        if (typeof value == 'number') {
            this._height = value;
            this.stage.height = this._height;

            this.gradient = this.stage.getContext('2d').createLinearGradient(0, 0, 0, value * .5);
            // Add color stops
            this.gradient.addColorStop(0, '#2196F3');
            this.gradient.addColorStop(1, '#4cbbed');
        }
    }
    get height() {
        return this._height || window.innerHeight;
    }

    set colour(value) {
        this._colour = value;
    }
    get colour() {
        return this._colour || "#18d618";
    }}


class SurfacePoint {
    constructor(index, acceleration, speed, height) {
        this.index = index;
        this.acceleration = acceleration;
        this.speed = speed;
        this.height = height;
    }

    set height(value) {
        if (typeof value == 'number') {
            this._height = value;
            // this._height = value > 300 ? 300 : (value < -300 ? -300 : value);
        }
    }
    get height() {
        return typeof this._height == 'number' ? this._height : 0;
    }
    set speed(value) {
        if (typeof value == 'number') {
            this._speed = Math.min(Math.max(value, -2), 2);
        }
    }
    get speed() {
        return typeof this._speed == 'number' ? this._speed : 0;
    }
    set acceleration(value) {
        if (typeof value == 'number') {
            this._acceleration = value;
        }
    }
    get acceleration() {
        return typeof this._acceleration == 'number' ? this._acceleration : 0;
    }}


surface = new Surface(window.innerWidth / 50, new Vector(window.innerWidth, window.innerHeight));
surface.colour = '#000000';

window.addEventListener('resize', () => {
    surface.dimensions = new Vector(window.innerWidth, window.innerHeight);
});

document.body.appendChild(surface.stage);