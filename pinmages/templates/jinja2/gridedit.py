<div class="gridedit">
    <div class="gridcomponent">
        {% for image in grid_data %}
        <div class="image">
            {{image.get('svg_data')}}
        </div>
        <div class="name">
            <input type="text">
        </div>
        <div class="tags">
            <input type="text">
        </div>
        <div class="description">
            <input type="text">
        </div>
        {% endfor %}
    </div>
</div>