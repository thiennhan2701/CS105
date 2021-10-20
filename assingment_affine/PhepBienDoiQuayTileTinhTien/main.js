
function init() {
    var scene = new THREE.Scene();

    var box = getBox(1, 1, 1);
    var plane = getPlane(4);

    plane.name = 'plane-1';

    box.position.y = box.geometry.parameters.height/2;
    plane.rotation.x = Math.PI/2;
    box.position.x = -5
    plane.position.y = 1;
    plane.add(box);
    scene.add(plane);

    var camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth/window.innerHeight,
        1, 
        1000
    );
    camera.position.z = 30;



    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    document.getElementById('webgl').appendChild(renderer.domElement);

    var controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.minDistance = 1;
    controls.maxDistance = 1000;

    update(renderer, scene, camera);
    return scene;
}

function getBox(w, h, d){
    var geometry = new THREE.BoxGeometry(w, h, d);

    var material = new THREE.MeshBasicMaterial({
        color: 'blue'
    });
    var mesh = new THREE.Mesh(
        geometry,
        material
    );

    return mesh;
}

function getPlane(size){
    var geometry = new THREE.PlaneGeometry(size, size);

    var material = new THREE.MeshBasicMaterial({
        color: 'pink',
        side: THREE.DoubleSide
    });
    var mesh = new THREE.Mesh(
        geometry,
        material
    );

    return mesh;
}
function update(renderer, scene, camera){
    renderer.render(
        scene,
        camera
    );

    var plane = scene.getObjectByName('plane-1');
    plane.rotation.y += 0.001;
    plane.rotation.z += 0.001;
    scene.traverse(function(child){
        child.scale.x += 0.001;
    })
    requestAnimationFrame(function(){
        update(renderer, scene, camera);
    })

}

var scene = init();

